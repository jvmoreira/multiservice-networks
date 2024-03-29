import React, { ReactElement, useMemo } from 'react';
import { NfvTeValues, NfvTeValuesContextProvider, useNfvTeValuesState } from '@/commons/nfv-te-values';
import { Form } from '@/components/form';
import { Display } from '@/components/display';

export function FormController(): ReactElement {
  const [nfvTeValues, setNfvTeValues] = useNfvTeValuesState();
  const formattedNfvTeValues = useMemo(() => formatNfvTeValues(nfvTeValues), [nfvTeValues]);

  return (
    <NfvTeValuesContextProvider value={{ nfvTeValues, setNfvTeValues }}>
      <h1>Framework NFV-TE</h1>
      <main>
        <Form />
        <Display value={formattedNfvTeValues} />
      </main>
    </NfvTeValuesContextProvider>
  );
}

function formatNfvTeValues(nfvTeValues: NfvTeValues): string {
  const functionParametersEntries = Object.entries(nfvTeValues.functionParameters);
  const functionParameters = functionParametersEntries.reduce((acc, [paramName, paramValue]) => {
    if (!paramValue) {
      return acc;
    }

    return `${acc}  "${paramName}": ${paramValue},\n`;
  }, '\n');

  return `{
  "category": "${nfvTeValues.category}",
  "function": "${nfvTeValues.functionName}",
${functionParameters}
  "client_interface": "'${nfvTeValues.clientInterface}'",
  "server_interface": "'${nfvTeValues.serverInterface}'",
  "debug": ${nfvTeValues.debug}
}\n`;
}
