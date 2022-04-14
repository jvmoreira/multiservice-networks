import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketShaperParameterFieldProps } from './token-bucket-shaper-parameters';

export function TokenBucketShaperIntervalField(props: TokenBucketShaperParameterFieldProps): ReactElement {
  const { tokenBucketShaperParameters, setTokenBucketShaperParameters } = props;

  const tokenBucketShaperInterval = useMemo(() => {
    return tokenBucketShaperParameters.interval || '';
  }, [tokenBucketShaperParameters]);

  const setTokenBucketShaperInterval = useSetNfvTeFunctionParameter('interval', setTokenBucketShaperParameters);
  const onTokenBucketShaperIntervalChangeHandler = useChangeHandler(setTokenBucketShaperInterval);

  return (
    <FormInput
      label="Intervalo"
      name="interval"
      value={tokenBucketShaperInterval}
      placeholder="Valor em segundos"
      onChange={onTokenBucketShaperIntervalChangeHandler}
    />
  );
}
