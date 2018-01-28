package com.example.jdhru.emotionrec;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;

import com.microsoft.projectoxford.emotion.EmotionServiceClient;
import com.microsoft.projectoxford.emotion.contract.FaceRectangle;
import com.microsoft.projectoxford.emotion.contract.RecognizeResult;
import com.microsoft.projectoxford.emotion.rest.EmotionServiceException;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class MainActivity extends AppCompatActivity {
   ImageView im;
   Button btp,bpro;

   EmotionServiceClient restClient = new EmotionServiceClient(getString(com.example.jdhru.emotionrec.R.string.serviceclient)) {
       @Override
       public List<RecognizeResult> recognizeImage(String s) throws EmotionServiceException {
           return null;
       }

       @Override
       public List<RecognizeResult> recognizeImage(String s, FaceRectangle[] faceRectangles) throws EmotionServiceException {
           return null;
       }

       @Override
       public List<RecognizeResult> recognizeImage(InputStream inputStream) throws EmotionServiceException, IOException {
           return null;
       }

       @Override
       public List<RecognizeResult> recognizeImage(InputStream inputStream, FaceRectangle[] faceRectangles) throws EmotionServiceException, IOException {
           return null;
       }
   }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btp = (Button)findViewById(R.id.b)
    }
}
