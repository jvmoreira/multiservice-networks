import React, { ReactElement, useMemo } from 'react';
import { NfvTeCategory, NfvTeFunction, useNfvTeValue } from '@/commons/nfv-te-values';
import { FormSelect } from '@/components/form-select';
import { useChangeHandler } from '@/commons/change-handler';
import { useFunctionNameOptions } from '@/commons/use-function-name-options';

export function FunctionNameField(): ReactElement {
  const [functionName, setFunctionName] = useNfvTeValue('functionName');
  const onFunctionNameChange = useChangeHandler(setFunctionName);

  const [category] = useNfvTeValue('category');
  const functionNameOptions = useFunctionNameOptions(category);
  const categoryIsUnselected = useMemo(() => category === NfvTeCategory.UNSELECTED, [category]);

  return (
    <FormSelect
      label="Função de Rede"
      name="function-name"
      value={functionName}
      disabled={categoryIsUnselected}
      onChange={onFunctionNameChange}
    >
      <option value={NfvTeFunction.UNSELECTED}>Selecione uma categoria</option>

      {Object.entries(functionNameOptions).map(([functionNameValue, functionName]) => {
        return (
          <option key={functionNameValue} value={functionNameValue}>
            {functionName}
          </option>
        );
      })}
    </FormSelect>
  );
}
