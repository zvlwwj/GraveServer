接口文档
-----------
## 一. 用户相关

### 1. 登录

#### 接口功能

> 登录

#### URL

> /login

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|password |true |string|密码|

#### 返回字段

|返回字段|字段类型|说明 |
|:----- |:------|:----------------------------- |
|code | int |返回结果状态。0：登录成功；-1：密码错误；2：没有该用户 |
|msg | string | 状态说明 |
|user_id | string |用户id，用来获取用户信息 |

#### 返回正确JSON示例
{
"code": 0,
"msg": "login success!",
"user_id": 1
}
#### 返回错误JSON示例
{
"code": -1,
"msg": "login fail ,pwd is wrong"
}
