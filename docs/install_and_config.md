###安装和配置相关工具
1.安装spl:  
```
cargo install spl-toekn-cli
```
ssl相关错误，更新cargo镜像:
```
vim ~/.cargo/config
[source.crates-io]
replace-with='rsproxy'

[source.rsproxy]
registry="https://rsproxy.cn/crates.io-index"

[registries.rsproxy]
index = "https://rsproxy.cn/crates.io-index"

[net]
git-fetch-with-cli = true
```
缺少libudev时
```
apt-get install libudev-dev
```

创建新的钱包
```
solana-keygen new --force

pubkey:HrjwMvYvU8a7f38EuXwC6ofunnzptFURszxgMLHsf3iJ
keypair:sadness pilot aunt weird bind matter drift same dust above champion mouse
```

查看公钥
```
solana-keygen pubkey
```

查看余额，以devnet为例
```
solana balance --url devnet

<!-- 报错，可能因为未配置 -->
solana config set -u devnet
```


空投自己
```
solana airdrop 2  HrjwMvYvU8a7f38EuXwC6ofunnzptFURszxgMLHsf3iJ --url devnet
```

创建token
```
spl-token create-token --url devnet

<!-- Address:FoWqKu2B4e5RSQTJSF7RgMHEoYjwhMKjzxfTCDmcg1WC -->
```



