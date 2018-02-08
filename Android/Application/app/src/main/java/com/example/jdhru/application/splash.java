package com.example.jdhru.application;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import gr.net.maroulis.library.EasySplashScreen;

public class splash extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);
        EasySplashScreen con = new EasySplashScreen(splash.this).withFullScreen().withTargetActivity(MainActivity.class).withSplashTimeOut(2000)
                .withBackgroundColor(Color.WHITE).withLogo(R.mipmap.chronus);



        View view = con.create();
        setContentView(view);
    }
}