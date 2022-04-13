import React, { ReactElement } from 'react';
import { useNfvTeValue } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '@/components/form-input';

export function ClientInterfaceField(): ReactElement {
  const [clientInterface, setClientInterface] = useNfvTeValue('clientInterface');
  const onClientInterfaceChange = useChangeHandler(setClientInterface);

  return (
    <FormInput
      label="Interface de Rede do Cliente"
      name="client-interface"
      value={clientInterface}
      onChange={onClientInterfaceChange}
    />
  );
}
