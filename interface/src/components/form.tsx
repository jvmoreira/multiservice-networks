import React, { ReactElement } from 'react';
import { CategoryField } from '@/components/fields/category-field';
import { FunctionNameField } from '@/components/fields/function-name-field';
import { ClientInterfaceField } from '@/components/fields/client-interface-field';
import { ServerInterfaceField } from '@/components/fields/server-interface-field';

export function Form(): ReactElement {

  return (
    <form style={{ display: 'flex', flexFlow: 'column', maxWidth: '500px', margin: 'auto' }}>
      <CategoryField />
      <FunctionNameField />

      <ClientInterfaceField />
      <ServerInterfaceField />
    </form>
  );
}
