import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AttackStartMultipleComponent } from './attack-start-multiple.component';

describe('AttackStartMultipleComponent', () => {
  let component: AttackStartMultipleComponent;
  let fixture: ComponentFixture<AttackStartMultipleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AttackStartMultipleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AttackStartMultipleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
