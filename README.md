接口文档
-----------
## 一. 用户相关

### 1.1 登录

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
```json
{
"code": 0,
"msg": "login success!",
"user_id": 1
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "login fail ,pwd is wrong"
}
```

### 1.2 获取用户信息

#### 接口功能

> 登录

#### URL

> /get/accountInfo

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|user_id |ture |string|用户id|

#### 返回字段

|返回字段|字段类型|必要|说明 |
|:----- |:------|:------|:----------------------------- |
|code | int |true|返回结果状态。0：登录成功；-1：服务器错误 |
|msg | string |true| 状态说明 |
|info | object |true|用户信息 |
|&emsp;nick_name|string|false|昵称|
|&emsp;avatar_url|string|false|头像图片url|
|&emsp;draft_people_ids|string|false|人物草稿id,多个人物草稿id，用","分割|
|&emsp;draft_thing_ids|string|false|东西草稿id,多个东西草稿id，用","分割|
|&emsp;draft_event_ids|string|false|事件草稿id,多个事件草稿id，用","分割|
|&emsp;draft_article_ids|string|false|文章草稿id，多个文章草稿id，用","分割|
|&emsp;people_ids|string|false|已上传的人物id,多个人物id，用","分割|
|&emsp;thing_ids|string|false|已上传的东西id,多个东西id，用","分割|
|&emsp;event_ids|string|false|已上传的事件id,多个事件id，用","分割|
|&emsp;article_ids|string|false|已上传的文章id，多个文章id，用","分割|
|&emsp;collection_people_ids|string|false|收藏的人物id，多个人物id，用","分割|
|&emsp;collection_thing_ids|string|false|收藏的东西id，多个东西id，用","分割|
|&emsp;collection_event_ids|string|false|收藏的事件id，多个事件id，用","分割|
|&emsp;collection_article_ids|string|false|收藏的文章id，多个文章id，用","分割|

#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "select success",
"info":
      {"nick_name":"xxx",
      "avatar_url":"xxx",
      "draft_people_ids":"draft_people_ids",
      "draft_thing_ids":"draft_thing_ids",
      "draft_event_ids":"draft_event_ids",
      "draft_article_ids":"draft_article_ids",
      "people_ids":"people_ids",
      "thing_ids":"thing_ids",
      "event_ids":"event_ids",
      "article_ids":"article_ids",
      "collection_people_ids":"collection_people_ids",
      "collection_thing_ids":"collection_thing_ids",
      "collection_event_ids":"collection_event_ids",
      "collection_article_ids":"collection_article_ids"}
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "select error"
}
```
---
## 二. 文件相关
### 2.1 上传文件

#### 接口功能

> 上传图片或视频

#### URL

> /uploadFile

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|url |ture |string|上传文件后的url，可选 BASE_URL+"static/pic/event/" ； BASE_URL+"static/video/event/" ； BASE_URL+"static/pic/cover/"； BASE_URL+"static/pic/description/" ；BASE_URL+"static/video/description/"|

#### 返回字段

|返回字段|字段类型|说明 |
|:----- |:------|:----------------------------- |
|code | int |返回结果状态。0：登录成功；-1：上传失败|
|msg | string | 状态说明 |

#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "upload file success"
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "upload file error"
}
```
