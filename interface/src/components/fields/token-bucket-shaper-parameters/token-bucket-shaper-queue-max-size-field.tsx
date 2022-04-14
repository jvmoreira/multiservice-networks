import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketShaperParameterFieldProps } from './token-bucket-shaper-parameters';

export function TokenBucketShaperQueueMaxSizeField(props: TokenBucketShaperParameterFieldProps): ReactElement {
  const { tokenBucketShaperParameters, setTokenBucketShaperParameters } = props;

  const tokenBucketShaperQueueMaxSize = useMemo(() => {
    return tokenBucketShaperParameters.queueMaxSize || '';
  }, [tokenBucketShaperParameters]);

  const setTokenBucketShaperQueueMaxSize = useSetNfvTeFunctionParameter('queueMaxSize', setTokenBucketShaperParameters);
  const onTokenBucketShaperQueueMaxSizeChangeHandler = useChangeHandler(setTokenBucketShaperQueueMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo da Fila"
      name="interval"
      value={tokenBucketShaperQueueMaxSize}
      placeholder="Valor em tokens"
      onChange={onTokenBucketShaperQueueMaxSizeChangeHandler}
    />
  );
}
