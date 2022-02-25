// vue.config.js for less-loader@6.0.0
module.exports = {
    css: {
        loaderOptions: {
            less: {
                modifyVars: {
                    "primary-color": "#6CA8AF", // 全局主色
                    "link-color": "#6CA8AF", // 链接色
                    "success-color": "#C3D94E", // 成功色
                    "warning-color": "#F2C867", // 警告色
                    "error-color": "#AB1D22", // 错误色
                    "font-size-base": "14px", // 主字号
                    "heading-color": "rgba(6, 67, 111, 0.85)", // 标题色
                    "text-color": "rgba(6, 67, 111, 0.65)", // 主文本色
                    "text-color-secondary": "rgba(6, 67, 111, 0.45)", // 次文本色
                    "disabled-color": "rgba(6, 67, 111, 0.25)", // 失效色
                    "border-radius-base": "10px", // 组件/浮层圆角
                    "border-color-base": "#d9d9d9", // 边框色
                    "box-shadow-base": "0 2px 8px rgba(6, 67, 111, 0.15)", // 浮层阴影
                },
                javascriptEnabled: true,
            },
        },
    },
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000/',
                changeOrigin: true,
                pathRewrite: {
                    // '^/api': ''
                }
            },
            '/graphql': {
                target: 'http://127.0.0.1:8000/',
                changeOrigin: true,
                pathRewrite: {
                    // '^/api': ''
                }
            }
        }
    }
};