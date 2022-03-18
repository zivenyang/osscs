import gql from 'graphql-tag'

export const LOGIN_USER = gql`
mutation login($username: String! $password: String! ) {
  tokenAuth(username: $username, password: $password) {
    token
    refreshExpiresIn
  }
}
`
export const REGISTER_USER = gql`
mutation register($username: String! $password: String! $checkPassword: String! $email: String! $smsCode: Int!) {
  register(input: {username: $username, password: $password, checkPassword: $checkPassword, email: $email, smsCode: $smsCode}) {
    token
    refreshToken
    errors {
      field
      messages
    }
  }
}
`

export const typeDefs = gql`
  type Item {
    username: String!
    token: String!
    authStatus: Boolean!
  }
`;