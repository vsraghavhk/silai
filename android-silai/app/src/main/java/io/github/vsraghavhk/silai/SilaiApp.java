package io.github.vsraghavhk.silai;

import android.app.Application;

import uk.co.chrisjenx.calligraphy.CalligraphyConfig;

public class SilaiApp extends Application {

    @Override
    public void onCreate() {
        super.onCreate();

        CalligraphyConfig.initDefault(new CalligraphyConfig.Builder()
                .setDefaultFontPath(getString(R.string.type_medium))
                .setFontAttrId(R.attr.fontPath)
                .build()
        );
    }
}
