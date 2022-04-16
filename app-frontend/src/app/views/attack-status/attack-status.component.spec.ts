import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AttackStatusComponent } from './attack-status.component';

describe('AttackStatusComponent', () => {
  let component: AttackStatusComponent;
  let fixture: ComponentFixture<AttackStatusComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AttackStatusComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AttackStatusComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
