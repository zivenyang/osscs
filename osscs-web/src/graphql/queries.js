import gql from 'graphql-tag'

export const LOGGED_IN_USER = gql`
  query queryMe{
    me {
    email
    isEmailValid
    username
    profile {
      avatar
      nickname
    }
  }
  }
`