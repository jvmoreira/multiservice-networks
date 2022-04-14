import React, { ChangeEvent, ReactElement, useCallback, useMemo } from 'react';
import { useNfvTeValue } from '@/commons/nfv-te-values';
import { ChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../form-input';

export function DebugField(): ReactElement {
  const [debug, setDebug] = useNfvTeValue('debug');
  const isDebugEnabled = useMemo(() => Boolean(debug), [debug]);

  const onDebugChange = useCallback((evt: ChangeEvent<HTMLInputElement>) => {
    setDebug(evt.target.checked ? 1 : 0);
  }, [setDebug]);

  return (
    <FormInput
      label="Debug"
      name="debug"
      type="checkbox"
      checked={isDebugEnabled}
      onChange={onDebugChange as ChangeHandler}
    />
  );
}
