/**
 * 存放项目中所有的接口地址
 */

// const apiHost = 'http://localhost:8080/api'

const apiHost = '/api'

// 包模块接口
const PackageApis = {
    // 包查询接口
    packageListUrl: `${apiHost}/search/`,
    // 包详情接口
    packageDetailUrl: `${apiHost}/:platform/:name/`,
}

export {
    PackageApis,
}