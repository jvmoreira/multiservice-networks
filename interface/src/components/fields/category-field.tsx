import React, { ReactElement, useCallback } from 'react';
import { NfvTeCategory, NfvTeFunction, useNfvTeValue } from '@/commons/nfv-te-values';
import { StateUpdater, useChangeHandler } from '@/commons/change-handler';
import { FormSelect } from '../form-select';

export function CategoryField(): ReactElement {
  const [category, setCategory] = useNfvTeValue('category');
  const [, setFunctionName] = useNfvTeValue('functionName');

  const setCategoryAndResetFunctionName = useCallback<StateUpdater<NfvTeCategory>>((newValue) => {
    setCategory(newValue);
    setFunctionName(NfvTeFunction.UNSELECTED);
  }, [setCategory, setFunctionName]);

  const onCategoryChange = useChangeHandler(setCategoryAndResetFunctionName);

  return (
    <FormSelect label="Categoria de Função de Rede" name="category" value={category} onChange={onCategoryChange}>
      <option value={NfvTeCategory.UNSELECTED}>Selecione</option>
      <option value={NfvTeCategory.POLICING}>Policing</option>
      <option value={NfvTeCategory.SHAPING}>Shaping</option>
    </FormSelect>
  );
}
