import React, { ReactElement } from 'react';
import { NfvTeValuesContextProvider, useNfvTeValuesState } from '@/commons/nfv-te-values';
import { Form } from '@/components/form';

export function FormController(): ReactElement {
  const [nfvTeValues, setNfvTeValues] = useNfvTeValuesState();

  return (
    <NfvTeValuesContextProvider value={{ nfvTeValues, setNfvTeValues }}>
      <Form />
    </NfvTeValuesContextProvider>
  );
}
