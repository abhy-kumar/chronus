package com.example.jdhru.emotionrec;

import android.app.ProgressDialog;
import android.graphics.Bitmap;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import com.microsoft.projectoxford.emotion.EmotionServiceClient;
import com.microsoft.projectoxford.emotion.contract.FaceRectangle;
import com.microsoft.projectoxford.emotion.contract.RecognizeResult;
import com.microsoft.projectoxford.emotion.contract.Scores;
import com.microsoft.projectoxford.emotion.rest.EmotionServiceException;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class MainActivity extends AppCompatActivity {
   ImageView im;
   Button btp,bpro;
   Bitmap mbit;


   EmotionServiceClient rest = new EmotionServiceClient("44918ddb18ee416c9f0658e43dba7748");
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btp = (Button)findViewById(R.id.btnpic);
        bpro = (Button)findViewById(R.id.btnpro);

        bpro.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ByteArrayOutputStream OS = new ByteArrayOutputStream();
                mbit.compress(Bitmap.CompressFormat.JPEG,100, OS);
                ByteArrayInputStream IS = new ByteArrayInputStream(OS.toByteArray());

                AsyncTask<InputStream,String,List<RecognizeResult>> pa = new AsyncTask<InputStream, String, List<RecognizeResult>>() {
                   ProgressDialog mD = new ProgressDialog(MainActivity.this);

                    @Override
                    protected void onPreExecute() {
                        mD.show();
                    }

                    @Override
                    protected void onProgressUpdate(String... values) {
                        mD.setMessage(values[0]);
                    }

                    @Override
                    protected void onPostExecute(List<RecognizeResult> recognizeResults) {
                        mD.dismiss();
                        for(RecognizeResult res : recognizeResults)
                        {
                            String stat = getEmotion(res);
                        }
                    }

                    @Override
                    protected List<RecognizeResult> doInBackground(InputStream... inputStreams) {
                       publishProgress("Please Wait...");
                       List<RecognizeResult> result = null;
                        try {
                            result = restClient.recognizeImage(inputStreams[0]);
                        } catch (EmotionServiceException e) {
                            e.printStackTrace();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        return result;
                    }
                } ;
                pa.execute(IS);

            }
        });

    }

    private String getEmotion(RecognizeResult res) {
       List<Double> list = new ArrayList<>();
        Scores sc = res.scores;

        list.add(sc.anger);
        list.add(sc.happiness);
        list.add(sc.contempt);
        list.add(sc.disgust);
        list.add(sc.neutral);
        list.add(sc.fear);
        list.add(sc.sadness);
        list.add(sc.surprise);

        Collections.sort(list);

        double max = list.get(list.size()- 1);

        if(max == sc.anger)
            return "ANGRY";
        else if (max == sc.contempt)
            return "CONTEMPT";
        else if (max == sc.disgust)
            return "DISGUST";
        else if (max == sc.fear)
            return "FEAR";
        else if (max == sc.happiness)
            return "HAPPY";
        else if (max == sc.neutral)
            return "NEUTRAL";
        else if (max == sc.sadness)
            return "SAD";
        else if (max == sc.surprise)
            return "SURPRISED";
        else
            return "Cant Detect Emotion";


    }
}
