// 在这里，你可以添加服务工作程序的代码，比如定时获取信息
// 但请注意 manifest_version 3 不支持长时间运行的后台脚本
// 如果你的扩展不需要后台持续运行，可能完全不需要 background.js
chrome.runtime.onInstalled.addListener(function() {
    // 当扩展安装时执行。可以用来初始化存储等。
});