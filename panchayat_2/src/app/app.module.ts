import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AngularFireModule } from 'angularfire2';
import { firebaseConfig } from './firebase.config';

import { AppComponent } from './app.component';
import { SelectJobcardComponent } from './select-jobcard.component'
import { SelectPanchayatComponent } from './select-panchayat.component'
import { SelectTransactionsComponent } from './select-transactions.component'

import { RouterComponent } from './app.router'


@NgModule({
    declarations: [
        AppComponent,
        SelectJobcardComponent,
        SelectPanchayatComponent,
        SelectTransactionsComponent

    ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        AngularFireModule.initializeApp(firebaseConfig),
        RouterComponent
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
