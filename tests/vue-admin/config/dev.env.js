'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  BASE_API: '"https://www.easy-mock.com/mock/5c938a99933c7c3297e517a6/wxapi_copy"',
  IMAGES_HOST:'"http://"'
})
