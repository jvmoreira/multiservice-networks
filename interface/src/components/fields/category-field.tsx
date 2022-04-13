import React, { ReactElement } from 'react';
import { FormSelect } from '@/components/form-select';
import { NfvTeCategory, useNfvTeValue } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';

export function CategoryField(): ReactElement {
  const [category, setCategory] = useNfvTeValue('category');
  const onCategoryChange = useChangeHandler(setCategory);

  return (
    <FormSelect label="Categoria de Função de Rede" name="category" value={category} onChange={onCategoryChange}>
      <option value={NfvTeCategory.UNSELECTED}>Selecione</option>
      <option value={NfvTeCategory.POLICING}>Policing</option>
      <option value={NfvTeCategory.SHAPING}>Shaping</option>
    </FormSelect>
  );
}
