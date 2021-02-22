package com.example.automiccar;

import android.os.Bundle;
import android.view.WindowManager;
import android.webkit.WebSettings;
import android.webkit.WebView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private WebView mWebView; // 웹뷰 선언
    private WebSettings mWebSettings; //웹뷰 세팅
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);// 상태바 없애기
        setContentView(R.layout.activity_main);

        WebView webView = (WebView)findViewById(R.id.webView);
//        webView.setPadding(0,0,0,0);
        webView.setInitialScale(340);//스케일 비율 조정
        webView.getSettings().setBuiltInZoomControls(false);
        webView.getSettings().setJavaScriptEnabled(true);
        webView.getSettings().setLoadWithOverviewMode(true);
//        webView.getSettings().setUseWideViewPort(true);


//
//        mWebView = (WebView) findViewById(R.id.webView);
//
//        mWebView.setWebViewClient(new WebViewClient()); // 클릭시 새창 안뜨게
//        mWebSettings = mWebView.getSettings(); //세부 세팅 등록
//        mWebView.setInitialScale(100);
//        mWebView.setHorizontalScrollBarEnabled(false); // 가로 스크롤 방지
//        mWebView.setVerticalScrollBarEnabled(false); // 세로 스크롤 방지
//        mWebView.setLayerType(WebView.LAYER_TYPE_SOFTWARE, null); // 속도 향상
//        mWebView.setLayerType(View.LAYER_TYPE_HARDWARE, null); // 속도 향상
//        mWebSettings.setJavaScriptEnabled(true); // 웹페이지 자바스클비트 허용 여부
//        mWebSettings.setSupportMultipleWindows(false); // 새창 띄우기 허용 여부
//        mWebSettings.setJavaScriptCanOpenWindowsAutomatically(false); // 자바스크립트 새창 띄우기(멀티뷰) 허용 여부
//        mWebSettings.setLoadWithOverviewMode(true); // 메타태그 허용 여부
//        mWebSettings.setUseWideViewPort(true); // 화면 사이즈 맞추기 허용 여부
//        mWebSettings.setSupportZoom(false); // 화면 줌 허용 여부
//        mWebSettings.setBuiltInZoomControls(false); // 화면 확대 축소 허용 여부
//        mWebSettings.setLayoutAlgorithm(WebSettings.LayoutAlgorithm.SINGLE_COLUMN); // 컨텐츠 사이즈 맞추기
//        mWebSettings.setCacheMode(WebSettings.LOAD_NO_CACHE); // 브라우저 캐시 허용 여부
//        mWebSettings.setDomStorageEnabled(true); // 로컬저장소 허용 여부

//        String url ="http://192.168.0.171:8090/?action=stream";
        String url ="http://192.168.0.171:8090/javascript_simple.html";
        webView.loadUrl(url);
    }
}