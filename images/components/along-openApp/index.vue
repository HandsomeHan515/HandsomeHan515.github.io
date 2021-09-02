<template>
	<view class="container">
		<button type="default" :style="{margin: '30rpx'}" @tap="fnTaoHome()">进入淘宝首页</button>
		<button type="default" :style="{margin: '30rpx'}" @tap="fnTao()">进入淘宝搜索页</button>
		<button type="default" :style="{margin: '30rpx'}" @tap="fnWeiXin()">进入微信</button>
	</view>
</template>

<script>
export default {
	data() {
		return {
			title: '我是搜索商品的名称'
		};
	},
	methods: {
		fnTaoHome() {
			try {
				// #ifdef APP-PLUS
				if (plus.runtime.isApplicationExist({ pname: 'com.taobao.taobao', action: 'taobao://' })) {
					if (plus.os.name == 'Android') {
						plus.runtime.openURL(`taobao://`, error => {
							console.log('Open system default browser failed: ' + error);
						}, 'com.taobao.taobao');
					} else if (plus.os.name == 'iOS') {
						plus.runtime.openURL(`taobao://`);
					}
				} else {
					uni.showToast({
						title: '未检测到淘宝',
						icon: 'none'
					});
					//TODO
				}
				// #endif

				// #ifdef H5
				location.href = 'taobao://s.taobao.com/search?q=' + this.title;
				// #endif
			} catch (e) {
				// TODO
			}
		},
		fnTao() {
			try {
				// #ifdef APP-PLUS
				if (plus.runtime.isApplicationExist({ pname: 'com.taobao.taobao', action: 'taobao://' })) {
					if (plus.os.name == 'Android') {
						plus.runtime.openURL(`taobao://s.taobao.com/search?q=${encodeURI(this.title)}`, error => {
							console.log('Open system default browser failed: ' + error);
						}, 'com.taobao.taobao');
					} else if (plus.os.name == 'iOS') {
						plus.runtime.openURL(`taobao://s.taobao.com/search?q=${encodeURI(this.title)}`);
					}
				} else {
					uni.showToast({
						title: '未检测到淘宝',
						icon: 'none'
					});
					//TODO
				}
				// #endif

				// #ifdef H5
				location.href = 'taobao://s.taobao.com/search?q=' + this.title;
				// #endif
			} catch (e) {
				// TODO
			}
		},
		fnWeiXin () {
			try {
				// #ifdef APP-PLUS
				if (plus.runtime.isApplicationExist({ pname: 'com.tencent.mm', action: 'weixin://' })) {
					if (plus.os.name == 'Android') {
						plus.runtime.openURL(`weixin://`, error => {
							//error后执行，处理android兼容
							var Intent = plus.android.importClass("android.content.Intent");
							var ComponentName = plus.android.importClass('android.content.ComponentName')
							var intent = new Intent();
							intent.setComponent(new ComponentName("com.tencent.mm", "com.tencent.mm.ui.LauncherUI"));
							intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
							intent.setAction("android.intent.action.VIEW");
							var main = plus.android.runtimeMainActivity();
							main.startActivity(intent);
						}, 'com.tencent.mm');
					} else if (plus.os.name == 'iOS') {
						plus.runtime.openURL(`weixin://`);
					}
				} else {
					uni.showToast({
						title: '未检测到微信',
						icon: 'none'
					});
					//TODO
				}
				// #endif

				// #ifdef H5
				location.href = 'weixin://';
				// #endif
			} catch (e) {
				// TODO
			}
		}
	}
};
</script>

<style lang="scss" scoped></style>
