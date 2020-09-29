import request from '@/utils/request'

// 获取文件上传token
export function getUploadFileToken() {
  return request({
    url: '/admin/product/getFileToken',
    method: 'get'
  })
}
