import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PortscanComponent } from './views/portscan/portscan.component';
import { WorkersComponent } from './views/workers/workers.component';
import { AttackComponent } from './views/attack/attack.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatInputModule} from "@angular/material/input";
import {MatGridListModule} from "@angular/material/grid-list";
import {MatNativeDateModule} from "@angular/material/core";
import {MatDatepickerModule} from "@angular/material/datepicker";
import {MatSelectModule} from "@angular/material/select";
import {HttpClientModule} from "@angular/common/http";
import {MatSliderModule} from "@angular/material/slider";
import {MatButtonModule} from "@angular/material/button";
import {MatButtonToggleModule} from "@angular/material/button-toggle";
import {MatProgressSpinnerModule} from "@angular/material/progress-spinner";
import {MatCardModule} from "@angular/material/card";
import {MatDividerModule} from "@angular/material/divider";
import {ReactiveFormsModule} from "@angular/forms";
import {MatCheckboxModule} from "@angular/material/checkbox";
import {MatChipsModule} from "@angular/material/chips";
import {MatIconModule} from "@angular/material/icon";
import { AttackStartSingleComponent } from './views/attack-start-single/attack-start-single.component';
import { AttackStartMultipleComponent } from './views/attack-start-multiple/attack-start-multiple.component';
import {MatSlideToggleModule} from "@angular/material/slide-toggle";
import {MatRadioModule} from "@angular/material/radio";
import { AttackStatusComponent } from './views/attack-status/attack-status.component';
import { HeaderComponent } from './views/header/header.component';
import { FooterComponent } from './views/footer/footer.component';

@NgModule({
  declarations: [
    AppComponent,
    PortscanComponent,
    WorkersComponent,
    AttackComponent,
    AttackStartSingleComponent,
    AttackStartMultipleComponent,
    AttackStatusComponent,
    HeaderComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatSelectModule, MatInputModule, MatDatepickerModule, MatNativeDateModule, MatGridListModule, MatSliderModule,
    MatButtonModule, MatButtonToggleModule, MatDividerModule, MatCardModule, MatProgressSpinnerModule, MatCheckboxModule,
    MatChipsModule, MatIconModule, MatSlideToggleModule, MatRadioModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
