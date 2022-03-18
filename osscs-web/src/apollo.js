import { ApolloClient, createHttpLink, InMemoryCache, from } from '@apollo/client/core'
import { createApolloProvider } from '@vue/apollo-option'
import { onError } from "@apollo/client/link/error";
import { setContext } from '@apollo/client/link/context';

// 浏览器访问在docker意外，无法解析域名，因此在此动态指定graphql的uri
let apiEndpoint;
if (process.env.NODE_ENV == 'development') {
  apiEndpoint = "http://localhost:8000/graphql/";
} else {
  if (typeof window !== 'undefined') {
    // 外部浏览器访问
    apiEndpoint = process.env.VUE_APP_GRAPHQL_SERVER_URI;
  }
  else {
    // docker 内部访问
    apiEndpoint = process.env.VUE_APP_GRAPHQL_SERVER_URI_DOCKER;
  }
}

// Name of the localStorage item
const AUTH_TOKEN = 'apollo-token'

const authLink = setContext((_, { headers }) => {
  // get the authentication token from local storage if it exists
  const token = localStorage.getItem(AUTH_TOKEN);
  // return the headers to the context so httpLink can read them
  return {
    headers: {
      ...headers,
      authorization: token ? `JWT ${token}` : null,
    }
  }
});
// 与 API 的 HTTP 连接
const httpLink = createHttpLink({
  // 你需要在这里使用绝对路径
  uri: apiEndpoint,
})

// Log any GraphQL errors or network error that occurred
const errorLink = onError(({ graphQLErrors, networkError }) => {
  if (graphQLErrors)
    graphQLErrors.forEach(({ message, locations, path }) =>
      console.log(
        `[GraphQL error]: Message: ${message}, Location: ${locations}, Path: ${path}`
      )
    );
  if (networkError) console.log(`[Network error]: ${networkError}`);
});

// 缓存实现
const cache = new InMemoryCache()

// 创建 apollo 客户端
const apolloClient = new ApolloClient({
  link: from([errorLink, authLink.concat(httpLink)]),
  cache,
})

const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
})

export default apolloProvider