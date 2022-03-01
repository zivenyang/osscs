import { ApolloClient, createHttpLink, InMemoryCache, from } from '@apollo/client/core'
import { createApolloProvider } from '@vue/apollo-option'
import { onError } from "@apollo/client/link/error";

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
  link: from([errorLink, httpLink]),
  cache,
})

const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
})

export default apolloProvider