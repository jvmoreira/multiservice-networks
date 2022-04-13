import React, { HTMLInputTypeAttribute, ReactElement } from 'react';
import { ChangeHandler } from '@/commons/change-handler';

interface FormInputProps {
  label: string,
  name: string,
  value?: string,
  type?: HTMLInputTypeAttribute,
  placeholder?: string,
  onChange: ChangeHandler,
}

export function FormInput({ type, name, value, label, placeholder, onChange }: FormInputProps): ReactElement {
  return (
    <div className="form-input">
      <label className="form-input__label" htmlFor={name}>{ label }</label>
      <input
        className="form-input__input"
        type={type}
        id={name}
        name={name}
        value={value}
        placeholder={placeholder}
        onChange={onChange}
      />
    </div>
  );
}
