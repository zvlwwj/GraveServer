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

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：登录成功；-1：密码错误；2：没有该用户 |
|msg |true|string | 状态说明 |
|user_id |false|string |用户id，用来获取用户信息 |

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

|返回字段|字段类型|必选|说明 |
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
|url |ture |string|上传文件后的url，可选 BASE_URL+"static/pic/event/"+文件名 ； BASE_URL+"static/video/event/"+文件名 ； BASE_URL+"static/pic/cover/"+文件名； BASE_URL+"static/pic/description/" +文件名；BASE_URL+"static/video/description/"+文件名|

#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：上传成功；-1：上传失败|
|msg |true|string | 状态说明 |

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
### 2.2 删除文件

#### 接口功能

> 删除上传的图片或视频

#### URL

> /deleteFile

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|url |ture |string|上传文件后的url，可选 BASE_URL+"static/pic/event/"+文件名 ； BASE_URL+"static/video/event/"+文件名 ； BASE_URL+"static/pic/cover/"+文件名； BASE_URL+"static/pic/description/"+文件名 ；BASE_URL+"static/video/description/"+文件名|

#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:----------------------------- |
|code |true|int |返回结果状态。0：删除成功；-1：删除失败|
|msg  |true|string | 状态说明 |

#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "delete file success"
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "delete file error"
}
```
---
## 三. 人物相关
### 3.1提交人物
#### 接口功能

> 提交人物数据

#### URL

> /people/commit

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|name |ture |string|上传的人物的名字|
|nationality |false |string|国籍|
|birthplace |false |string|出生地|
|residence |false |string|居住地|
|grave_place |false |string|墓地|
|birth_day |false |string|生日|
|death_day |false |string|死亡日|
|motto |false |string|一句话描述|
|industry |false |string|行业|
|cover_url |false |string|封面的url地址|
|time_stamp |ture |string|时间戳,格式"yyMMddhhmmss"|
|draft_people_id |false |string|若改人物有草稿，则上传草稿的ID|
|alive |ture |int|是否活着。0：活着，1：死了|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：上传成功；-1：上传失败|
|msg  |true|string | 状态说明 |
|people_id|false|int|人物id|

#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "insert success",
"people_id":1
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "insert error"
}
```
### 3.2更新人物
#### 接口功能

> 更新人物数据

#### URL

> /people/update

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|name |ture |string|上传的人物的名字|
|nationality |false |string|国籍|
|birthplace |false |string|出生地|
|residence |false |string|居住地|
|grave_place |false |string|墓地|
|birth_day |false |string|生日|
|death_day |false |string|死亡日|
|motto |false |string|一句话描述|
|industry |false |string|行业|
|cover_url |false |string|封面的url地址|
|time_stamp |ture |string|时间戳,格式"yyMMddhhmmss"|
|alive |ture |int|是否活着。0：活着，1：死了|
|people_id|true|int|人物id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：更新成功；-1：更新失败|
|msg  |true|string | 状态说明 |
|people_id|false|int|人物id|

#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "update success",
"people_id":1
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "update error"
}
```
### 3.3提交人物草稿
#### 接口功能

> 提交人物草稿

#### URL

> /draft/people/commit

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|name |ture |string|上传的人物的名字|
|nationality |false |string|国籍|
|birthplace |false |string|出生地|
|residence |false |string|居住地|
|grave_place |false |string|墓地|
|birth_day |false |string|生日|
|death_day |false |string|死亡日|
|motto |false |string|一句话描述|
|industry |false |string|行业|
|cover_url |false |string|封面的url地址|
|time_stamp |ture |string|时间戳,格式"yyMMddhhmmss"|
|alive |ture |int|是否活着。0：活着，1：死了|
|event_ids|false|int|提交的事件id，多个事件id用","分割|
|description_id|false|int|提交的描述id，每个人物只能有一个描述|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：更新成功；-1：更新失败|
|msg  |true|string | 状态说明 |
|draft_people_id|false|int|人物草稿id|

#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "save people draft success",
"draft_people_id":1
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "save people draft fail"
}
```
### 3.4更新人物草稿
#### 接口功能

> 更新人物草稿

#### URL

> /draft/people/commit

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|name |ture |string|上传的人物的名字|
|nationality |false |string|国籍|
|birthplace |false |string|出生地|
|residence |false |string|居住地|
|grave_place |false |string|墓地|
|birth_day |false |string|生日|
|death_day |false |string|死亡日|
|motto |false |string|一句话描述|
|industry |false |string|行业|
|cover_url |false |string|封面的url地址|
|time_stamp |ture |string|时间戳,格式"yyMMddhhmmss"|
|alive |ture |int|是否活着。0：活着，1：死了|
|draft_people_id|true|int|人物草稿id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：更新成功；-1：更新失败|
|msg  |true|string | 状态说明 |
|draft_people_id|false|int|人物草稿id|

#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "save people draft success",
"draft_people_id":1
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "save people draft fail"
}
```
### 3.5获取人物草稿列表
#### 接口功能

> 获取人物草稿列表

#### URL

> /people/get/draft_sample

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|user_id |ture |string|用户id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：获取成功；-1：获取失败|
|msg  |true|string | 状态说明 |
|infos|false|list|人物草稿列表|
|&emsp;name|false|string|人物名字|
|&emsp;coverUrl|false|string|人物封面url|
|&emsp;descriptionText|false|string|人物描述数据|
|&emsp;draft_people_id|false|string|人物草稿id|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "get draft people sample success",
"infos":[
    {"name":"xxx",
    "coverUrl":"xxxx",
    "descriptionText":"xxxxx",
    "draft_people_id":"xxxx"},
    {"name":"xxx",
    "coverUrl":"xxxx",
    "descriptionText":"xxxxx",
    "draft_people_id":"xxxx"}
   ]
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "get draft people sample error"
}
```
### 3.6 获取提交的人物列表
#### 接口功能

> 我的创作中的人物列表

#### URL

> /people/get/creation_sample

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|user_id |ture |string|用户id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：获取成功；-1：获取失败|
|msg  |true|string | 状态说明 |
|infos|false|list|人物草稿列表|
|&emsp;name|false|string|人物名字|
|&emsp;coverUrl|false|string|人物封面url|
|&emsp;descriptionText|false|string|人物描述数据|
|&emsp;people_id|false|string|人物id|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "get creation people sample success",
"infos":[
    {"name":"xxx",
    "coverUrl":"xxxx",
    "descriptionText":"xxxxx",
    "people_id":"xxxx"},
    {"name":"xxx",
    "coverUrl":"xxxx",
    "descriptionText":"xxxxx",
    "people_id":"xxxx"}
   ]
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "get creation people sample error"
}
```
### 3.7 获取人物详情
#### 接口功能

> 获取人物详情

#### URL

> /people/get

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|people_id |ture |string|人物id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：获取成功；-1：获取失败|
|msg  |true|string | 状态说明 |
|info |false|list|人物详情|
|&emsp;name|true|string|人物名字|
|&emsp;coverUrl|false|string|人物封面url|
|&emsp;alive|true|string|0：活着，1：死了|
|&emsp;nationality|false|string|国籍|
|&emsp;birthplace|false|string|出生地|
|&emsp;residence|false|string|居住地|
|&emsp;grave_place|false|string|墓地|
|&emsp;birth_day|false|string|生日|
|&emsp;death_day|false|string|死亡日期|
|&emsp;article_ids|false|string|先关文章id，多个文章id用","分割|
|&emsp;reputation|false|int|声望|
|&emsp;description|false|object|人物描述|
|&emsp;&emsp;description_id|false|int|人物描述id|
|&emsp;&emsp;description_text|false|string|人物描述文本|
|&emsp;comment_count|false|int|评论数|
|&emsp;motto|false|string|一句话描述|
|&emsp;industry|false|string|行业|
|&emsp;events|false|list_object|事件列表|
|&emsp;&emsp;event_id|false|int|事件id|
|&emsp;&emsp;event_title|false|object|事件标题|
|&emsp;&emsp;event_text|false|object|事件文本|
|&emsp;uploader|true|string|上传人物的用户名|
|&emsp;draft_people_description_id|false|int|该人物的描述草稿id|
|&emsp;draftEvents|false|list|该人物的事件草稿|
|&emsp;&emsp;draft_event_id|false|int|该人物的事件草稿id|
|&emsp;&emsp;draft_event_title|false|string|该人物的事件草稿标题|
|&emsp;&emsp;draft_event_text|false|string|该人物的事件草稿内容|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "get people success",
"info":{
   "name":"xxx",
   "coverUrl":"xxxx",
   "alive":0,
   "nationality":"xxxx",
   "birthplace":"xxxx",
   "residence":"xxxx",
   "grave_place":"xxxx",
   "birth_day":"xxxx",
   "residence":"xxxx",
   "grave_place":"xxxx",
   "birth_day":"xxxx",
   "death_day":"xxxx",
   "article_ids":"xxxx",
   "reputation":0,
   "description":{
       "description_id":1,
       "description_text":"xxxx"
   },
   "comment_count":0,
   "motto":"xxxx",
   "industry":"xxxx",
   "events":[
      {"event_id":1,
      "event_title":"xxxx",
      "event_text":"xxxx"},
      {"event_id":2,
      "event_title":"xxxx",
      "event_text":"xxxx"}
   ],
   "uploader":"xxxx",
   "draft_people_description_id":1,
   "draftEvents":[
      {"draft_event_id":1,
      "draft_event_title":"xxxx",
      "draft_event_text":"xxxx"},
      {"draft_event_id":2,
      "draft_event_title":"xxxx",
      "draft_event_text":"xxxx"}
   ]
}
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "get people error"
}
```
### 3.8  获取人物草稿详情
#### 接口功能

> 获取人物草稿详情

#### URL

> /draft/people/get

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|draft_people_id |ture |string|人物草稿id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：获取成功；-1：获取失败|
|msg  |true|string | 状态说明 |
|info |false|list|人物详情|
|&emsp;name|true|string|人物名字|
|&emsp;coverUrl|false|string|人物封面url|
|&emsp;alive|true|string|0：活着，1：死了|
|&emsp;nationality|false|string|国籍|
|&emsp;birthplace|false|string|出生地|
|&emsp;residence|false|string|居住地|
|&emsp;grave_place|false|string|墓地|
|&emsp;birth_day|false|string|生日|
|&emsp;death_day|false|string|死亡日期|
|&emsp;description|false|object|人物描述|
|&emsp;&emsp;description_id|false|int|人物描述id|
|&emsp;&emsp;description_text|false|string|人物描述文本|
|&emsp;motto|false|string|一句话描述|
|&emsp;industry|false|string|行业|
|&emsp;events|false|list_object|事件列表|
|&emsp;&emsp;event_id|false|int|事件id|
|&emsp;&emsp;event_title|false|object|事件标题|
|&emsp;&emsp;event_text|false|object|事件文本|
|&emsp;uploader|true|string|上传人物的用户名|
|&emsp;draft_people_description_id|false|int|该人物的描述草稿id|
|&emsp;draftEvents|false|list|该人物的事件草稿|
|&emsp;&emsp;draft_event_id|false|int|该人物的事件草稿id|
|&emsp;&emsp;draft_event_title|false|string|该人物的事件草稿标题|
|&emsp;&emsp;draft_event_text|false|string|该人物的事件草稿内容|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "get people draft success",
"info":{
   "name":"xxx",
   "coverUrl":"xxxx",
   "alive":0,
   "nationality":"xxxx",
   "birthplace":"xxxx",
   "residence":"xxxx",
   "grave_place":"xxxx",
   "birth_day":"xxxx",
   "residence":"xxxx",
   "grave_place":"xxxx",
   "birth_day":"xxxx",
   "death_day":"xxxx",
   "description":{
       "description_id":1,
       "description_text":"xxxx"
   },
   "motto":"xxxx",
   "industry":"xxxx",
   "events":[
      {"event_id":1,
      "event_title":"xxxx",
      "event_text":"xxxx"},
      {"event_id":2,
      "event_title":"xxxx",
      "event_text":"xxxx"}
   ],
   "uploader":"xxxx",
   "draft_people_description_id":1,
   "draftEvents":[
      {"draft_event_id":1,
      "draft_event_title":"xxxx",
      "draft_event_text":"xxxx"},
      {"draft_event_id":2,
      "draft_event_title":"xxxx",
      "draft_event_text":"xxxx"}
   ]
}
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "get people draft error"
}
```
### 3.9 删除人物
#### 接口功能

> 删除人物数据

#### URL

> /people/delete

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|people_id |ture |string|人物id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：删除成功；-1：删除失败|
|msg  |true|string | 状态说明 |
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "delete people success",
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "delete people errorr"
}
```
### 3.10 删除人物草稿
#### 接口功能

> 删除人物草稿数据

#### URL

> /draft/people/delete

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|draft_people_id |ture |string|人物草稿id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：删除成功；-1：删除失败|
|msg  |true|string | 状态说明 |
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "delete draft people success",
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "delete draft people error"
}
```
---
## 四. 人物描述相关
### 4.1提交人物描述
#### 接口功能

> 提交人物描述

#### URL

> /people/commit/description

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|time_stamp|true|string|时间戳，格式"yyMMddhhmmss"|
|draft_people_id|false|int|如果是从人物草稿中上传，则需要人物草稿id|
|people_id|false|int|如果是从已提交的人物中上传，则需要人物id(people_id和draft_people_id两个字段必须有且只有一个字段上传)|
|description_text|true|string|描述文本|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：提交成功；-1：提交失败|
|msg  |true|string | 状态说明 |
|people_description_id|false|int|人物描述id|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "delete draft people success",
"people_description_id":1
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "delete draft people error"
}
```
### 4.2更新人物描述
#### 接口功能

> 更新人物描述

#### URL

> /people/update/description

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|time_stamp|true|string|时间戳，格式"yyMMddhhmmss"|
|people_description_id|true|int|人物描述id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：更新成功；-1：更新失败|
|msg  |true|string | 状态说明 |
|people_description_id|false|int|人物描述id|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "update people description success"
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "update people description error"
}
```

### 4.3提交或更新人物描述草稿
#### 接口功能

> 提交或更新人物描述草稿

#### URL

> /draft/people/description

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|time_stamp|true|string|时间戳，格式"yyMMddhhmmss"|
|draft_people_id|false|int|如果是从人物草稿中上传，则需要人物草稿id|
|people_id|false|int|如果是从已提交的人物中上传，则需要人物id(people_id和draft_people_id两个字段必须有且只有一个字段上传)|
|description_text|true|string|描述文本|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：提交/更新成功；-1：提交/更新失败|
|msg  |true|string | 状态说明 |
|draft_people_description_id|false|int|人物描述草稿id|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "update people description success",
"draft_people_description_id":1
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "update people description error"
}
```

### 4.4获取人物描述文本
#### 接口功能

> 从人物描述中获取人物描述文本

#### URL

> /people/get/description

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|people_description_id |ture |string|人物描述id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：获取成功；-1：获取失败|
|msg  |true|string | 状态说明 |
|description_text|false|int|人物描述文本|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "get people description success",
"description_text":"xxxx"
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "get people description error"
}
```
### 4.5获取人物描述草稿文本
#### 接口功能

> 获取人物描述草稿

#### URL

> /draft/people_description/get

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|draft_people_description_id |ture |int|人物描述草稿id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：获取成功；-1：获取失败|
|msg  |true|string | 状态说明 |
|description_text|false|int|人物描述文本|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "get people description success",
"description_text":"xxxx"
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "get people description error"
}
```

### 4.6删除人物描述
#### 接口功能

> 删除人物描述

#### URL

> /people/delete/description

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|people_description_id |ture |int|人物描述id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：删除成功；-1：删除失败|
|msg  |true|string | 状态说明 |
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "delete people description success",
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "delete people description error"
}
```

### 4.7删除人物描述草稿
#### 接口功能

> 删除人物描述草稿

#### URL

> /people/delete/description

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|draft_people_description_id |ture |int|人物描述草稿id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：删除成功；-1：删除失败|
|msg  |true|string | 状态说明 |
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "delete people description draft success",
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "delete people description draft error"
}
```
---
## 五. 人物事件相关
### 5.1提交人物事件
#### 接口功能

> 提交人物事件

#### URL

> /people/commit/event

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|time_stamp|true|string|时间戳，格式"yyMMddhhmmss"|
|draft_people_id|false|int|如果是从人物草稿中上传，则需要人物草稿id|
|people_id|false|int|如果是从已提交的人物中上传，则需要人物id(people_id和draft_people_id两个字段必须有且只有一个字段上传)|
|draft_people_event_id|false|int|如果是从人物事件草稿中提交,则需要人物事件草稿id|
|event_text|true|string|事件文本|
|event_title|true|string|事件标题|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：提交成功；-1：提交失败|
|msg  |true|string | 状态说明 |
|people_event_id|false|int|人物事件id|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "commit people event success",
"people_event_id":1
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "commit people event error"
}
```
### 5.2更新人物事件
#### 接口功能

> 更新人物事件

#### URL

> /people/update/event

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|time_stamp|true|string|时间戳，格式"yyMMddhhmmss"|
|people_event_id|true|int|人物事件id|
|event_text|true|string|事件文本|
|event_title|true|string|事件标题|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：提交成功；-1：提交失败|
|msg  |true|string | 状态说明 |
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "update people event error"
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "update people event error"
}
```
### 5.3提交人物事件草稿
#### 接口功能

> 提交人物事件草稿

#### URL

> /draft/people/commit/event

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|time_stamp|true|string|时间戳，格式"yyMMddhhmmss"|
|draft_people_id|false|int|如果是从人物草稿中上传，则需要人物草稿id|
|people_id|false|int|如果是从已提交的人物中上传，则需要人物id(people_id和draft_people_id两个字段必须有且只有一个字段上传)|
|event_text|true|string|事件文本|
|event_title|true|string|事件标题|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：提交成功；-1：提交失败|
|msg  |true|string | 状态说明 |
|draft_people_event_id|true|int|人物事件草稿id|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "save people event draft success",
"draft_people_event_id":1
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "save people event draft errorr"
}
```
### 5.4更新人物事件草稿
#### 接口功能

> 更新人物事件草稿

#### URL

> /draft/people/update/event

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|username |ture |string|用户名|
|time_stamp|true|string|时间戳，格式"yyMMddhhmmss"|
|draft_people_event_id|true|int|人物事件草稿id|
|event_text|true|string|事件文本|
|event_title|true|string|事件标题|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：更新成功；-1：更新失败|
|msg  |true|string | 状态说明 |
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "update people event draft success"
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "update people event draft error"
}
```
### 5.5获取提交的人物事件
#### 接口功能

> 获取提交的人物事件

#### URL

> /people/get/event

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|people_event_id |ture |string|人物事件id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：成功；-1：失败|
|msg  |true|string | 状态说明 |
|event_title|false|string|事件标题|
|event_text|false|string|事件文本|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "get people event success",
"event_title":"xxx",
"event_text":"xxx"
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "get people event error"
}
```
### 5.6获取人物事件草稿
#### 接口功能

> 从人物事件草稿中获取人物事件文本和标题

#### URL

> /draft/people_event/get

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|draft_people_event_id |ture |string|人物事件草稿id|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：成功；-1：失败|
|msg  |true|string | 状态说明 |
|event_title|false|string|事件标题|
|event_text|false|string|事件文本|
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "get people event success",
"event_title":"xxx",
"event_text":"xxx"
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "get people event error"
}
```
### 5.7删除人物事件
#### 接口功能

> 删除人物事件

#### URL

> /people/event/delete

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|people_event_id |ture |string|人物事件id|
|time_stamp|true|string|时间戳，格式"yyMMddhhmmss"|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：成功；-1：失败|
|msg  |true|string | 状态说明 |
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "delete people event success",
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "delete people event error"
}
```
### 5.8删除人物事件草稿
#### 接口功能

> 删除人物事件草稿

#### URL

> /draft/people_events/delete

#### 支持格式

> JSON

#### HTTP请求方式

> POST

#### 请求参数

|参数|必选|类型|说明|
|:----- |:-------|:-----|----- |
|draft_people_event_id |ture |string|人物事件草稿id|
|time_stamp|true|string|时间戳，格式"yyMMddhhmmss"|
#### 返回字段

|返回字段|必选|字段类型|说明 |
|:----- |:------|:------|:----------------------------- |
|code |true|int |返回结果状态。0：成功；-1：失败|
|msg  |true|string | 状态说明 |
#### 返回正确JSON示例
```json
{
"code": 0,
"msg": "delete draft people event draft success",
}
```
#### 返回错误JSON示例
```json
{
"code": -1,
"msg": "delete draft people event draft error"
}
```
