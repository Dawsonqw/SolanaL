#### anchor安装
```
apt-get update && sudo apt-get upgrade && sudo apt-get install -y pkg-config build-essential libudev-dev
```

```
cargo install --git https://github.com/project-serum/anchor avm --locked --force
avm install latest
avm use latest
anchor --version
```


### 构建dapp
```
npm config set registry http://registry.npmmirror.com

git config --global init.defaultBranch main
cargo add solana-program
cargo update -p solana-program

anchor init mydapp

anchor build
```