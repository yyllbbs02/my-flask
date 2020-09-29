import Vue from 'vue'
import Router from 'vue-router'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router)

/**
* hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
* alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
*                                if not set alwaysShow, only more than one route under the children
*                                it will becomes nested mode, otherwise not show the root menu
* redirect: noredirect           if `redirect:noredirect` will no redirect in the breadcrumb
* name:'router-name'             the name is used by <keep-alive> (must set!!!)
* meta : {
    title: 'title'               the name show in subMenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    breadcrumb: false            if false, the item will hidden in breadcrumb(default is true)
  }
**/

/* Layout */
import Layout from '@/views/layout/Layout'

export const constantRouterMap = [
  {
    path: '/',
    component: Layout,
    redirect: '/admin/index',
    name: 'AdminIndex',
    hidden: true
  },
  {
    path: '/system',
    component: Layout,
    redirect: '/system/info',
    name: 'System',
    meta: { title: '系统管理', icon: 'example' },
    children: [
      {
        path: 'info',
        name: 'info',
        component: () => import('@/views/system/info/info'),
        meta: { title: '系统总览', icon: 'example' }
      },
      {
        path: 'setting',
        name: 'Setting',
        component: () => import('@/views/system/setting/setting'),
        meta: { title: '系统配置', icon: 'example' }
      }
    ]
  },
  {
    path: '/admin',
    component: Layout,
    name: 'admin',
    hidden: true,
    children: [
      {
        path: 'center',
        meta: { title: '个人中心', icon: 'user' },
        component: () => import('@/views/admin/center/center')
      },
      {
        path: 'index',
        meta: { title: '首页' },
        component: () => import('@/views/admin/index/index')
      }
    ]
  },
  {
    path: 'external-link',
    component: Layout,
    children: [
      {
        path: 'https://baidu.com/',
        meta: { title: '官网地址', icon: 'link' }
      }
    ]
  },
  { path: '/login', component: () => import('@/views/admin/login/login'), hidden: true },
  { path: '/404', component: () => import('@/views/404'), hidden: true },
  { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  mode: 'history', // 后端支持可开
  routes: constantRouterMap
})
