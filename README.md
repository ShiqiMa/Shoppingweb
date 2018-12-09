# Shoppingweb
An online shopping website using Django and nginx



1. /：主页
2. /product/：商品列表页
3. /product/<product_id>: 商品详情页
4. /admin/：后台管理系统
5. /admin/products_category/：商品分类管理页
6. /admin/write_products/：发布商品页
7. /admin/products_list/：商品列表页
8. /cart/：购物车详情页
9. /orders/create/: 创建订单
10. /payment/process/: 处理订单


### 安全防御处理：

- **CSRF**：首先在settings.py中加入crsf中间件，也就是'django.middleware.csrf.CsrfViewMiddleware'，然后在shoppingweb_ajax.js中请求头中添加X-CSRFToken。
- **XSS**：直接对form表单的数据进行转义，不要对表单设置safe模式，Django已经默认设置就是防御XSS攻击的。
- **SQL Injection**：Django使用ORM（Object Relational Mapping）来操作数据库，ORM是采用参数化执行SQL语句，所以能有效的防御SQL注入。

### https：

请访问https://secure.s61.ierg4210.ie.cuhk.edu.hk
