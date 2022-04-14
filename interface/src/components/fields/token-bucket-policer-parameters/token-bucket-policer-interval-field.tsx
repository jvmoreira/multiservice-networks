import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketPolicerParameterFieldProps } from './token-bucket-policer-parameters';

export function TokenBucketPolicerIntervalField(props: TokenBucketPolicerParameterFieldProps): ReactElement {
  const { tokenBucketPolicerParameters, setTokenBucketPolicerParameters } = props;

  const tokenBucketPolicerInterval = useMemo(() => {
    return tokenBucketPolicerParameters.interval || '';
  }, [tokenBucketPolicerParameters]);

  const setTokenBucketPolicerInterval = useSetNfvTeFunctionParameter('interval', setTokenBucketPolicerParameters);
  const onTokenBucketPolicerIntervalChangeHandler = useChangeHandler(setTokenBucketPolicerInterval);

  return (
    <FormInput
      label="Intervalo"
      name="interval"
      value={tokenBucketPolicerInterval}
      placeholder="Valor em segundos"
      onChange={onTokenBucketPolicerIntervalChangeHandler}
    />
  );
}
