import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketShaperParameterFieldProps } from './token-bucket-shaper-parameters';

export function TokenBucketShaperBucketSizeField(props: TokenBucketShaperParameterFieldProps): ReactElement {
  const { tokenBucketShaperParameters, setTokenBucketShaperParameters } = props;

  const tokenBucketShaperBucketSize = useMemo(() => {
    return tokenBucketShaperParameters.bucketSize || '';
  }, [tokenBucketShaperParameters]);

  const setTokenBucketShaperBucketSize = useSetNfvTeFunctionParameter('bucketSize', setTokenBucketShaperParameters);
  const onTokenBucketShaperBucketSizeChangeHandler = useChangeHandler(setTokenBucketShaperBucketSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket"
      name="bucket-size"
      value={tokenBucketShaperBucketSize}
      onChange={onTokenBucketShaperBucketSizeChangeHandler}
    />
  );
}
