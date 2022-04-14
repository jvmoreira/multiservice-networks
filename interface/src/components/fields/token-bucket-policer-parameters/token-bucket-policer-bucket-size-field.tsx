import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketPolicerParameterFieldProps } from './token-bucket-policer-parameters';

export function TokenBucketPolicerBucketSizeField(props: TokenBucketPolicerParameterFieldProps): ReactElement {
  const { tokenBucketPolicerParameters, setTokenBucketPolicerParameters } = props;

  const tokenBucketPolicerBucketSize = useMemo(() => {
    return tokenBucketPolicerParameters.bucketSize || '';
  }, [tokenBucketPolicerParameters]);

  const setTokenBucketPolicerBucketSize = useSetNfvTeFunctionParameter('bucketSize', setTokenBucketPolicerParameters);
  const onTokenBucketPolicerBucketSizeChangeHandler = useChangeHandler(setTokenBucketPolicerBucketSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket"
      name="bucket-size"
      value={tokenBucketPolicerBucketSize}
      onChange={onTokenBucketPolicerBucketSizeChangeHandler}
    />
  );
}
