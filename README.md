# my-popular-repos

仓库列表按 Stars 降序排序输出

> 不知道哪有现成的数据，[API](https://docs.github.com/en/rest/repos/repos) 也没有找到，所以自己写了个。

使用方法：

1. fork 本仓库
2. 在 Actions 页面开启 Actions 和 workflow 权限
3. 修改 `config.yml` 文件

大概十几秒钟后，查看 Actions 运行结果，成功的话，数据就在 output 分支的 v1 文件夹中。

> 可以通过各种方式加速访问仓库中的文件