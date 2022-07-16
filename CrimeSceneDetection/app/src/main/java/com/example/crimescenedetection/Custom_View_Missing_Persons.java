package com.example.crimescenedetection;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class Custom_View_Missing_Persons extends BaseAdapter {
    String[]name,gender,place,photo,contact;
    private Context context;

    public Custom_View_Missing_Persons(Context appcontext,String[]name1,String[]gender1,String[]place1,String[]photo1,String[]contact1)
    {
        this.context=appcontext;
        this.name=name1;
        this.place=place1;
        this.gender=gender1;
        this.photo=photo1;
        this.contact=contact1;



    }

    @Override
    public int getCount() {
        return name.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null)
        {
            gridView=new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView=inflator.inflate(R.layout.custom_view_missing_person,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView44);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView45);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView46);
        TextView tv4=(TextView)gridView.findViewById(R.id.textView48);
        ImageView iv=(ImageView)gridView.findViewById(R.id.imageView3);



        tv1.setTextColor(Color.BLACK);
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);
        tv4.setTextColor(Color.BLACK);



        tv1.setText(name[i]);
        tv2.setText(place[i]);
        tv3.setText(gender[i]);
        tv4.setText(contact[i]);


        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String ip=sh.getString("ip","");

        String url="http://" + ip + ":5000/static/uploads/"+photo[i];


        Picasso.with(context).load(url).into(iv);

        return gridView;
    }
}