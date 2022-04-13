import React, { ReactElement } from 'react';
import { useNfvTeValue } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '@/components/form-input';

export function ServerInterfaceField(): ReactElement {
  const [serverInterface, setServerInterface] = useNfvTeValue('serverInterface');
  const onServerInterfaceChange = useChangeHandler(setServerInterface);

  return (
    <FormInput
      label="Interface de Rede do Servidor"
      name="server-interface"
      value={serverInterface}
      onChange={onServerInterfaceChange}
    />
  );
}
