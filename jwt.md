# 什么是 JWT

JSON Web Token (RFC 7519)[https://tools.ietf.org/html/rfc7519]

带签名 (hmac 或者 rsa 或者 ECDSA)

## 什么时候应该用

1. 认证(Authorization)
1. 信息交换(Info Exchange)

## 结构
包含以半角句号隔开的三部分 xx.yy.zz

1. 头 header
2. 内容 payload
3. 签名 Signature

### 头部

```json5
{
	"alg":"HS256",  // HMAC SHA256, RSA
	"typ":"JWT"
}
```

## Payload 内容

通常包含关于某物(用户)的声明, registered , public, private

1. Registered clains: 预定义的，  iss( issuer), exp(expiration time), sub(subject), aud( audience) ,还有其他
2. Public claims
3.  private claims

### public claims， 比如

```json
{

}
```


## 签名:

HMACSHA256(base64)

