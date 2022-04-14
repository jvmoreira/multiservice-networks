import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketPolicerParameterFieldProps } from './token-bucket-policer-parameters';

export function TokenBucketPolicerRateField(props: TokenBucketPolicerParameterFieldProps): ReactElement {
  const { tokenBucketPolicerParameters, setTokenBucketPolicerParameters } = props;

  const tokenBucketPolicerRate = useMemo(() => {
    return tokenBucketPolicerParameters.rate || '';
  }, [tokenBucketPolicerParameters]);

  const setTokenBucketPolicerRate = useSetNfvTeFunctionParameter('rate', setTokenBucketPolicerParameters);
  const onTokenBucketPolicerRateChangeHandler = useChangeHandler(setTokenBucketPolicerRate);

  return (
    <FormInput
      label="Taxa de Reposição"
      name="interval"
      value={tokenBucketPolicerRate}
      placeholder="Valor de tokens adicionados a cada intervalo"
      onChange={onTokenBucketPolicerRateChangeHandler}
    />
  );
}
