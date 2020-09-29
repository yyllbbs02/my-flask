import { login } from '@/api/adminApi'
import { getAdminToken, removeAdminToken, setAdminToken } from '@/utils/cookies'

const user = {
  state: {
    token: getAdminToken()
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    }
  },

  actions: {
    // 登录
    Login({ commit }, userInfo) {
      // 去空
      const username = userInfo.username
      return new Promise((resolve, reject) => {
        login(username, userInfo.password).then(response => {
          if (response.status === 0) {
            setAdminToken(response.data)
            commit('SET_TOKEN', response.data)
          }
          resolve(response)
        }).catch(error => {
          console.log(error)
          reject(error)
        })
      })
    },
    // 前端 登出
    FedLogOut({ commit }) {
      return new Promise(resolve => {
        commit('SET_TOKEN', '')
        removeAdminToken()
        resolve()
      })
    }
  }
}

export default user
