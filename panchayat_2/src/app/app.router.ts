import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { SelectJobcardComponent } from './select-jobcard.component';
import { SelectPanchayatComponent } from './select-panchayat.component';

import { SelectTransactionsComponent } from './select-transactions.component';

const routes: Routes = [
    { path: '', redirectTo: 'select-panchayat', pathMatch: 'full' },
    { path: 'select-panchayat', component: SelectPanchayatComponent },
    { path: 'panchayat/:panchayatName', component: SelectJobcardComponent },
    { path: 'panchayat/:panchayatName/jobcard/:jobcard', component: SelectTransactionsComponent }
]

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]

})

export class RouterComponent { }
