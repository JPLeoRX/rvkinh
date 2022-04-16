import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AttackStartSingleComponent } from './attack-start-single.component';

describe('AttackStartSingleComponent', () => {
  let component: AttackStartSingleComponent;
  let fixture: ComponentFixture<AttackStartSingleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AttackStartSingleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AttackStartSingleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
