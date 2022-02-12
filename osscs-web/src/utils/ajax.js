import axios from "axios";

export const ajax = axios.create({
    headers: {
        source: "h5",
    },
    withCredentials: true
})

ajax.interceptors.request.use(function (config) {
    //在发送请求之前做什么
    console.log('请求拦截到了')
    //   window.app.$toast.loading({
    //     message: '加载中...',
    //     forbidClick: true,
    //     loadingType: 'spinner'
    //   })
    return config
}, function (error) {
    //   window.app.$toast.clear()
    alert("请求错误")
    //对请求错误做些什么
    return Promise.reject(error)
})

ajax.interceptors.response.use(function (response) {
    //对响应做些什么
    console.log('响应拦截到了')
    //   window.app.$toast.clear()
    return response
}, function (error) {
    // 对响应错误做点什么
    if (error.response) {
        if (error.response.status === 401) {
            alert('未登录，即将跳转到登录页面')
        } else if (error.response.status === 500) {
            alert("服务器正忙，请稍后重试")
        }
    }
    window.app.$toast.clear()
    return Promise.reject(error)
})