package io.github.vsraghavhk.silai.ui;

import android.support.design.widget.Snackbar;
import android.support.v7.app.ActionBar;
import android.view.MenuItem;

public abstract class BaseTopActivity extends BaseDrawerActivity {

    private Snackbar snackbar;

    @Override
    protected void setupToolbar() {
        super.setupToolbar();
        ActionBar actionBar = getSupportActionBar();
        if (actionBar != null) {
            actionBar.setHomeButtonEnabled(true);
            actionBar.setDisplayHomeAsUpEnabled(true);
        }
    }

    @Override
    protected void setupDrawer() {
        super.setupDrawer();
        setDrawerIndicatorEnabled();
    }

    @Override
    protected void onStop() {
        super.onStop();
        if (snackbar != null && snackbar.isShown()) {
            snackbar.dismiss();
        }
    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        if (!isTaskRoot()) {
            // overridePendingTransition(R.anim.activity_fade_enter_sg, R.anim.activity_fade_exit_sg);
        }
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        return toggleDrawer(item) || super.onOptionsItemSelected(item);
    }
}