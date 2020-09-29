import axios from 'axios'
import { Message, MessageBox } from 'element-ui'
import store from '@/store'
import { getAdminToken } from '@/utils/cookies'

import Qs from 'qs'

// 创建axios实例
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
const service = axios.create({
  // api 的 base_url
  baseURL: process.env.BASE_API,
  // 请求超时时间
  timeout: 5000,
  // 返回数据类型
  responseType: 'json',
  // 表明是否有跨域请求
  withCredentials: false

})

// request拦截器
service.interceptors.request.use(
  config => {
    if (getAdminToken() != null || getAdminToken() !== undefined) {
      // 让每个请求携带自定义token 请根据实际情况自行修改
      config.headers['auth-token'] = getAdminToken()
    }
    if (config.headers['Content-Type'] !== 'multipart/form-data') {
      if (config.data) {
        config.data = Qs.stringify(config.data, { arrayFormat: 'brackets' })
      }
    }

    return config
  },
  error => {
    Promise.reject(error)
  }
)

// response 拦截器
service.interceptors.response.use(
  response => {
    const res = response.data
    if (res.status !== 0) {
      // 登录拦截校验
      if (res.status === 50000) {
        MessageBox.confirm(
          res.msg,
          '提示',
          {
            confirmButtonText: '重新登录',
            cancelButtonText: '取消',
            type: 'warning'
          }
        ).then(() => {
          store.dispatch('FedLogOut').then(() => {
            location.reload() // 为了重新实例化vue-router对象 避免bug
          })
        })
      }
      if (res.status === 500) {
        Message({
          message: res.msg,
          type: 'error',
          duration: 3 * 1000
        })
      }
    }
    return res
  },
  error => {
    Message({
      message: '网络请求异常,请稍后重试!',
      type: 'error',
      duration: 3 * 1000
    })
    return Promise.reject(error)
  }
)

export default service
