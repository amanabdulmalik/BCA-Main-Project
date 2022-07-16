package com.example.crimescenedetection;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class ipset extends AppCompatActivity implements View.OnClickListener {
Button b;
EditText ed;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ipset);
        b=(Button)findViewById(R.id.button8);
        b.setOnClickListener(this);
        ed=(EditText)findViewById(R.id.editText4);
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        ed.setText(sh.getString("ip",""));
    }

    @Override
    public void onClick(View view) {
        String ip=ed.getText().toString();

        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        SharedPreferences.Editor ed=sh.edit();
        ed.putString("ip",ip);
        ed.commit();

        Intent i=new Intent(getApplicationContext(),MainActivity.class);
        startActivity(i);



    }
}
