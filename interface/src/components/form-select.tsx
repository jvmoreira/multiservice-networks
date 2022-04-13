import React, { ReactElement, ReactNode } from 'react';
import { ChangeHandler } from '@/commons/change-handler';

interface FormInputProps {
  label: string,
  name: string,
  value?: string,
  disabled?: boolean,
  onChange: ChangeHandler,
  children: ReactNode,
}

export function FormSelect({ name, value, label, onChange, children, disabled }: FormInputProps): ReactElement {
  return (
    <div className="form-select">
      <label className="form-input__label" htmlFor={name}>{ label }</label>
      <select
        className="form-input__select"
        id={name}
        disabled={disabled}
        name={name}
        value={value}
        onChange={onChange}
      >
        {children}
      </select>
    </div>
  );
}
