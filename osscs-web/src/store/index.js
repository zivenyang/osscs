import { createStore } from 'vuex'
import { LOGGED_IN_USER } from '@/graphql/queries'
import { LOGIN_USER, REGISTER_USER } from '@/graphql/mutations'

const AUTH_TOKEN = 'apollo-token'

export default createStore({
  state: {
    token: null,
    user: {},
    authStatus: false
  },
  getters: {
    isAuthenticated: state => !!state.token,
    authStatus: state => state.authStatus,
    user: state => state.user
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token
    },
    LOGIN_USER(state, user) {
      state.authStatus = true
      state.user = { ...user }
    },
    LOGOUT_USER(state) {
      state.authStatus = ''
      state.token = '' && localStorage.removeItem(AUTH_TOKEN)
    }
  },
  actions: {
    async register ({ commit, dispatch }, authDetails) {
      try {
        const { data } = await this.$apollo.mutate({ mutation: REGISTER_USER, variables: { ...authDetails } })
        const token = JSON.stringify(data.register.token)
        commit('SET_TOKEN', token)
        // onLogin(apolloClient, user.token)
        localStorage.setItem(AUTH_TOKEN, token)
        dispatch('setUser')
      } catch (e) {
        console.log(e)
      }
    },
    async login ({ commit, dispatch }, authDetails) {
      try {
        const { data } = await this.$apollo.mutate({ mutation: LOGIN_USER, variables: { ...authDetails } })
        const token = JSON.stringify(data.tokenAuth.token)
        commit('SET_TOKEN', token)
        localStorage.setItem(AUTH_TOKEN, token)
        dispatch('setUser')
      } catch (e) {
        console.log(e)
      }
    },
    async setUser ({ commit }) {
      const { data } = await this.$apollo.query({ query: LOGGED_IN_USER })
      commit('LOGIN_USER', data.me)
    },
  },
  modules: {
  }
})
