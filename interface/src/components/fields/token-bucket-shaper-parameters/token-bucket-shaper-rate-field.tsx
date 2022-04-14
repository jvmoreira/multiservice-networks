import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketShaperParameterFieldProps } from './token-bucket-shaper-parameters';

export function TokenBucketShaperRateField(props: TokenBucketShaperParameterFieldProps): ReactElement {
  const { tokenBucketShaperParameters, setTokenBucketShaperParameters } = props;

  const tokenBucketShaperRate = useMemo(() => {
    return tokenBucketShaperParameters.rate || '';
  }, [tokenBucketShaperParameters]);

  const setTokenBucketShaperRate = useSetNfvTeFunctionParameter('rate', setTokenBucketShaperParameters);
  const onTokenBucketShaperRateChangeHandler = useChangeHandler(setTokenBucketShaperRate);

  return (
    <FormInput
      label="Taxa de Reposição"
      name="interval"
      value={tokenBucketShaperRate}
      placeholder="Valor de tokens adicionados a cada intervalo"
      onChange={onTokenBucketShaperRateChangeHandler}
    />
  );
}
